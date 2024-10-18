<script lang="ts">
    import type {Player} from "../utils/types";

    export let players: Player[]
</script>

<div class="scoreboard">
    <div class="wrapper">
        <div class="left-player">
            <div class="score"><span class="score-inner">{players[0].score}</span></div>
            <div class="player-info"><span class="player"><span class="team">{players[0].teamName}</span> {players[0].playerName}</span></div>
        </div>
        <div class="right-player">
            <div class="player-info"><span class="player"><span class="team">{players[1].teamName}</span> {players[1].playerName}</span></div>
            <div class="score"><span class="score-inner">{players[1].score}</span></div>
        </div>
    </div>
</div>

<style>
    .scoreboard {
        width: 1080px;
    }
    .wrapper, .left-player, .right-player {
        display: grid;
    }
    .wrapper {
        width: 90%;
        grid-template-columns: 1fr 1fr;
    }
    .left-player, .right-player {
        width: 50%;
    }
    .left-player {
        grid-template-columns: 1fr 6fr;
        transform: skewX(30deg);
    }
    .right-player {
        grid-template-columns: 6fr 1fr;
    }
    .player-info .player, .score-inner {
        display: block;
    }
    .left-player .player-info .player, .left-player .score-inner {
        transform: skewX(-30deg);
    }
    .right-player {
        transform: skewX(-30deg);
    }
    .right-player .player-info .player, .right-player .score-inner {
        transform: skewX(30deg);
    }
    .left-player .player-info {
        text-align: left;
    }
    .right-player .player-info {
        text-align: right;
    }
    .score {
        background: #EB0405;
        color: #FFED97;
    }
    .left-player .player-info {
        background: #FFED97;
    }
    .left-player .player-info, .right-player .player-info {
        color: #000;
    }
    .left-player .player-info .team {
        color: #235BA8;
    }
    .right-player .player-info {
        background: #235BA8
    }
    .right-player .team {
        color: #FFED97;
    }
</style>