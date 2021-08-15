<script>
    // IMPORTS
    import EditMeetup from "./Meetups/EditMeetup.svelte";
    import Header from "./UI/Header.svelte";
    import MeetupGrid from "./Meetups/MeetupGrid.svelte";
    import Button from "./UI/Button.svelte";

    // VARIABLES
    let editMode;

    // FUNCTIONS
    function closeModal() {
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
            on:addmeetup={closeModal}
            on:cancel={closeModal}
        />
    {/if}
    <MeetupGrid />
</main>

<style>
    main {
        margin-top: 5rem;
    }
</style>
