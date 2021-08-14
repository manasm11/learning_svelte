<script>
    import MeetupItem from "./MeetupItem.svelte";

    export let meetups;

    function handleFavorite(event) {
        const obj = {...meetups.find(m=>m.id==event.detail)}
        obj.isFavorite = !obj.isFavorite
        const newMeetups = [...meetups]
        newMeetups[meetups.findIndex(m=>m.id==event.detail)] = obj
        meetups = newMeetups
    }
</script>

<section id="meetups">
    {#each meetups as meetup(meetup.id)}
        <MeetupItem on:favorite={handleFavorite} {...meetup}/>
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