<script>

    // IMPORTS
    const MarkdownIt = require('markdown-it');

    // PROP
    export let title = "";
    export let content = "";

    // CONSTANTS
    const markdown = new MarkdownIt();

    // VARIABLES
    $:rendered = markdown.render(content);


    // DEBUGGING
    // $:(()=>console.log({content, rendered}))()
</script>

{#if title}
    <h1 class="text-3xl mb-3">{title}</h1>
{:else}
    <h1 class="text-3xl mb-3 text-gray-600">No title</h1>
{/if}

<div class="rendered">
    {#if content}
        {@html rendered}
    {:else}
        <p class="text-gray-600">No content</p>
    {/if}
</div>
