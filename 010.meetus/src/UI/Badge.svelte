<script>
    import {fade} from 'svelte/transition'
    import {cubicIn} from 'svelte/easing'
    export let text=' ';
</script>
<span transition:fade={{duration: 200, easing:cubicIn}}>{text}</span>

<style>
    span {
        background: var(--primary);
        color: white;
        padding: 0.1rem 1rem;
        font-size: 1rem;
        border-radius: 5px;
    }
</style>