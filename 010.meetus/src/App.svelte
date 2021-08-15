<script>
    // IMPORTS
    import EditMeetup from "./Meetups/EditMeetup.svelte";
    import Header from "./UI/Header.svelte";
    import MeetupGrid from "./Meetups/MeetupGrid.svelte";
    import Button from "./UI/Button.svelte";
    import MeetupDetail from "./Meetups/MeetupDetail.svelte";

    // VARIABLES
    let editMode;
    let page = "overview";
    let pageData = {};

    // FUNCTIONS
    function closeModal() {
        editMode = undefined;
    }

    function showDetail(event) {
        page = "detail";
        pageData = { id: event.detail.id };
    }

    function closeDetail() {
        page = "overview";
        pageData = {};
    }
</script>

<Header />

<main>
    {#if page === "overview"}
        <center>
            <Button on:click={() => (editMode = "add")}>Add New Meetup</Button>
        </center>
        {#if editMode === "add"}
            <EditMeetup on:addmeetup={closeModal} on:cancel={closeModal} />
        {/if}
        <MeetupGrid on:showdetail={showDetail} />
    {:else}
        <MeetupDetail id={pageData.id} on:closedetail={closeDetail} />
    {/if}
</main>

<style>
    main {
        margin-top: 5rem;
    }
</style>
