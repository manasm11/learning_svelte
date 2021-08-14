<script>
    import FormControl from "./FormControl.svelte";
    import Button from "../UI/Button.svelte";
    import Modal from "../UI/Modal.svelte";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let form_data;
    resetFormData();

    function resetFormData() {
        form_data = {
            id: "",
            title: "",
            subtitle: "",
            address: "",
            contactEmail: "",
            imageUrl: "",
            description: "",
        };
    }

    function submitForm() {
        dispatch("addmeetup", form_data);
        resetFormData();
    }
</script>

<Modal title="Add New Meetup" on:cancel>
    <form>
        {#each Object.keys(form_data) as form}
            <FormControl type={form} bind:value={form_data[form]} />
        {/each}
    </form>
    <div slot="footer">
        <Button mode="outline" on:click={() => dispatch("cancel")}>Cancel</Button>
        <Button on:click={submitForm}>Save</Button>
    </div>
</Modal>

<style>
    form {
        width: 100%;
    }
</style>
