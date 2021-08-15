<script>
    import meetups from './meetups-store'
    import MeetupItem from "./MeetupItem.svelte";

    function handleFavorite(event) {
        meetups.toggleFavourite(event.detail)
        
    }
</script>

<section id="meetups">
    {#each $meetups as meetup(meetup.id)}
        <MeetupItem {...meetup}/>
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