<script lang="ts">
  import {onMount} from "svelte";
  import {Router, Route} from "svelte-routing";
  import Home from "./routes/Home.svelte";
  import Update from "./routes/Update.svelte";
  import Login from "./routes/Login.svelte";
  import Scoreboard from "./routes/Scoreboard.svelte";
  import Commentators from "./routes/Commentators.svelte";

  let loggedIn: boolean | null;

  onMount(() => {
    loggedIn = !!localStorage.getItem("token");
  })

  export let url: string = "";
</script>

<Router {url}>
  <main>
    {#if loggedIn}
      <Route path="/" component={Home} />
      <Route path="/update" component={Update} />
    {:else}
      <Route path="/" component={Login} />
    {/if}
    <Route path="/scoreboard" component={Scoreboard} />
    <Route path="/commentators" component={Commentators} />
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
