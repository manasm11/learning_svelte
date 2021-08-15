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
        editMode = null;
        pageData = {}
    }

    function showDetail(event) {
        page = "detail";
        pageData = { id: event.detail.id };
    }

    function closeDetail() {
        page = "overview";
        pageData = {};
    }

    function edit(event) {
        editMode = 'edit'
        pageData = {id: event.detail.id}
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
        {:else if editMode === 'edit'}
            <EditMeetup on:addmeetup={closeModal} on:cancel={closeModal} id={pageData.id}/>
        {/if}
        <MeetupGrid on:showdetail={showDetail} on:edit={edit} />
    {:else}
        <MeetupDetail id={pageData.id} on:closedetail={closeDetail} />
    {/if}
</main>

<style>
    main {
        margin-top: 5rem;
    }
</style>
