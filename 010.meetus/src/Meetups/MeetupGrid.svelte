<script>
    import meetups from './meetups-store'
    import {flip} from 'svelte/animate'
    import MeetupItem from "./MeetupItem.svelte";
</script>

<section id="meetups">
    {#each $meetups as meetup(meetup.id)}
    <div animate:flip={{duration:500}}>
        <MeetupItem {...meetup} on:showdetail on:edit/>
    </div>
    {/each}
</section>

<style>
    section {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr;
        grid-gap: 1rem;
    }

    @media (min-width: 768px) {
        section {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>