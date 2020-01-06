import random

from django.shortcuts import render, redirect

from .models import Player, Game, PlayerGameInfo
from .forms import NumberForm


def show_home(request):
    template = 'home.html'

    player = request.session.get('player_id', 0)
    game = request.session.get('game_id', 0)

    if not player:
        new_player = Player.objects.create()
        request.session['player_id'] = new_player.id

    if not game:
        player_exist = Player.objects.get(id=player)
        if not player_exist:
            player_exist = new_player
        game_exist = Game.objects.filter(exist=True)
        if game_exist:
            PlayerGameInfo.objects.create(player=player_exist,
                                          game=game_exist[0],
                                          author=False)
            request.session['game_id'] = game_exist[0].id
            form = NumberForm()
            context = {'game_exist': True, 'form': form}
        else:
            count = random.randint(1, 10)
            game = Game.objects.create(exist=True,
                                       count=count)
            PlayerGameInfo.objects.create(player=player_exist,
                                          game=game,
                                          author=True)
            context = {'count': count}
            request.session['game_id'] = game.id
        return render(request, template, context)

    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            game_info = PlayerGameInfo.objects.get(player=player,
                                                   game=game)
            game_info.try_count += 1
            game_info.save()
            game = Game.objects.get(id=game)
            person_number = form.cleaned_data['number']
            if person_number == game.count:
                game.exist = False
                game.save()
                game_info.winner = True
                game_info.save()
                context = {'winner': True}
            elif person_number > game.count:
                context = {
                    'less': True,
                    'person_number': person_number,
                    'game_exist': True,
                    'form': form
                }
            else:
                context = {
                    'more': True,
                    'person_number': person_number,
                    'game_exist': True,
                    'form': form
                }
            return render(request, template, context)

    current_game = Game.objects.get(id=game)
    current_player = PlayerGameInfo.objects.get(player=player,
                                                game=game)
    if current_game.exist:
        if current_player.author:
            context = {'count': current_game.count}
        else:
            form = NumberForm()
            context = {
                'game_exist': True,
                'form': form
            }
        return render(request, template, context)
    else:
        if current_player.author:
            player = PlayerGameInfo.objects.get(game=game,
                                                author=False,
                                                winner=True)
            context = {
                'victory': True,
                'count': current_game.count,
                'try_count': player.try_count
            }
            del request.session['game_id']
            return render(request, template, context)
        else:
            del request.session['game_id']
            return redirect(show_home)
