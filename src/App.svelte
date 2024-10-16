<script lang="ts">
  import {onDestroy, onMount} from "svelte";
  import {Router, Route} from "svelte-routing";
  import {io, Socket} from "socket.io-client";}
  import Home from "./routes/Home.svelte";
  import Update from "./routes/Update.svelte";
  import Login from "./routes/Login.svelte";
  import Scoreboard from "./routes/Scoreboard.svelte";
  import Commentators from "./routes/Commentators.svelte";
  import type {Commentator, Player, ScoreboardResponse} from "./utils/types";
  import axios from "axios";
  import {objectToCamel} from "ts-case-convert";
  import {getToken} from "./utils/tokenService";

  let loggedIn: boolean | null;
  let socket: Socket | null;

  const retrieveScoreboard = async (): Promise<void> => {
    const { data } = await axios.get<ScoreboardResponse>("/api/scoreboard");
    players = objectToCamel(data.player_scores);
    commentators = objectToCamel(data.commentator_info);
  }

  onMount(() => {
    loggedIn = !!getToken();
    if (loggedIn) {
      retrieveScoreboard();
    }
    socket = io();
    socket.on('connect', () => {
      console.log('connection established')
    })
    socket.on('scoreboard_updated', () => {
      retrieveScoreboard();
    })
  })

  let players: Player[] = []
  let commentators: Commentator[] = []

  let url: string = "";
  onDestroy(() => {
    socket?.disconnect()
    console.log('connection closed')
  })
</script>

<Router {url}>
  <main>
    {#if loggedIn}
      <Route path="/" component={Home} />
      <Route path="/update"><Update {players} {commentators} /></Route>
    {:else}
      <Route path="/"><Login {loggedIn} /></Route>
    {/if}
    <Route path="/scoreboard"><Scoreboard {players} /></Route>
    <Route path="/commentators"><Commentators {commentators} /></Route>
  </main>
</Router>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>
