<script>
    // IMPORTS
    import EditMeetup from "./Meetups/EditMeetup.svelte";
    import Header from "./UI/Header.svelte";
    import meetups_data from "./DummyData/meetups";
    import MeetupGrid from "./Meetups/MeetupGrid.svelte";
    import Button from "./UI/Button.svelte";

    // VARIABLES
    let meetups = [...meetups_data];
    let editMode;

    // FUNCTIONS
    function addMeetup(event) {
        const form_data = event.detail;
        form_data.id = Math.random().toString();
        meetups = [{ ...form_data, id: Math.random().toString() }, ...meetups];
        editMode = undefined;
    }
</script>

<Header />

<main>
    <center>
        <Button on:click={() => (editMode = "add")}>Add New Meetup</Button>
    </center>
    {#if editMode === "add"}
        <EditMeetup
            on:addmeetup={addMeetup}
            on:cancel={() => (editMode = null)}
        />
    {/if}
    <MeetupGrid bind:meetups />
</main>

<style>
    main {
        margin-top: 5rem;
    }
</style>
