<script>
    import Header from "./UI/Header.svelte";
    import meetups_data from "./DummyData/meetups";
    import MeetupGrid from "./Meetups/MeetupGrid.svelte";
    import FormControl from "./Meetups/FormControl.svelte";
    import Button from './UI/Button.svelte'

    let meetups = [...meetups_data];

    let form_data = {
        id: "",
        title: "",
        subtitle: "",
        address: "",
        contactEmail: "",
        imageUrl: "",
        description: "",
    };

    function addMeetup() {
        form_data.id = Math.random().toString();
        meetups = [{ ...form_data, id: Math.random().toString() }, ...meetups];
        for (const k in form_data) {
            form_data[k] = "";
        }
    }
</script>

<Header />

<main>
    <form on:submit|preventDefault={addMeetup}>
        {#each Object.keys(form_data) as form}
            <FormControl type={form} bind:value={form_data[form]} />
        {/each}
        <Button>Save</Button>
    </form>
    <MeetupGrid {meetups} />
</main>

<style>
    main {
        margin-top: 5rem;
    }

    form {
        width: 30rem;
        max-width: 90%;
        margin: auto;
    }
</style>
