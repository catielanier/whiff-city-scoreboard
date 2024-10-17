<script lang="ts">
    import type {Player} from "../utils/types";

    export let players: Player[]
</script>

<div class="scoreboard">
    <div class="left-player">
        <div class="score">{players[0].score}</div>
        <div class="player-info"><span class="team">{players[0].teamName}</span> {players[0].playerName}</div>
    </div>
    <div class="right-player">
        <div class="player-info"><span class="team">{players[1].teamName}</span> {players[1].playerName}</div>
        <div class="score">{players[1].score}</div>
    </div>
</div>