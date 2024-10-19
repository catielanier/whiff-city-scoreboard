<script lang="ts">
    import {onDestroy, onMount} from "svelte";
    import {io, type Socket} from "socket.io-client";
    import {retrieveCommentators} from "../utils/api";
    import type {Commentator} from "../utils/types";

    let commentators: Commentator[];
    let socket: Socket | null;

    onMount(async () => {
        commentators = await retrieveCommentators();

        socket = io();
        socket?.on('connect', () => {
            console.log('connection established')
        })
        socket?.on('scoreboard_updated', async () => {
            commentators = await retrieveCommentators();
        })
    })

    onDestroy(() => {
        socket?.disconnect()
        console.log('connection closed')
    })
</script>

<div class="commentators">
    {#if commentators?.length}
        <div class="wrapper">
            <div class="left-commentator">
                <div class="commentator-name">
                    <span class="team-name">{commentators[0].teamName}</span> {commentators[0].commentatorName}
                </div>
                <div class="commentator-socials">
                    @{commentators[0].xHandle}
                </div>
            </div>
            <div class="right-commentator">
                <div class="commentator-name">
                    <span class="team-name">{commentators[1].teamName}</span> {commentators[1].commentatorName}
                </div>
                <div class="commentator-socials">
                    @{commentators[1].xHandle}
                </div>
            </div>
        </div>
    {/if}
</div>