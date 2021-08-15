<script>
    import FormControl from "./FormControl.svelte";
    import Button from "../UI/Button.svelte";
    import Modal from "../UI/Modal.svelte";
    import { createEventDispatcher } from "svelte";
    import meetups from './meetups-store'
    import { isNotEmpty, isValidEmail } from "../helpers/validators";
    const dispatch = createEventDispatcher();

    export let id = null;

    let form_data;
    resetFormData();
    if(id){
        form_data = $meetups.find(m=>m.id === id)
    }

    let are_valid = {
        id: true,
        title: false,
        subtitle: false,
        address: false,
        contactEmail: false,
        imageUrl: false,
        description: false,
        isFavorite: true
    }

    $: console.log(disabled)
    $: disabled = (()=>{
        for(let f in are_valid){
            if(!are_valid[f]){
                return true
            }
        }
        return false
    })()

    const form_validars = {
        id: [],
        title: [isNotEmpty],
        subtitle: [isNotEmpty],
        address: [isNotEmpty],
        contactEmail: [isNotEmpty, isValidEmail],
        imageUrl: [isNotEmpty],
        description: [isNotEmpty],
        isFavorite: []
    };

    function resetFormData() {
        form_data = {
            id: "",
            title: "",
            subtitle: "",
            address: "",
            contactEmail: "",
            imageUrl: "",
            description: "",
            isFavorite: "",
        };
    }

    function submitForm() {
        meetups.addMeetup(form_data)
        dispatch("addmeetup");
        resetFormData();
    }
</script>

<Modal title="Add New Meetup" on:cancel>
    <form>
        {#each Object.keys(form_data) as form}
            <FormControl
                type={form}
                bind:value={form_data[form]}
                validators={form_validars[form]}
                bind:valid={are_valid[form]}
            />
        {/each}
    </form>
    <div slot="footer">
        <Button mode="outline" on:click={() => dispatch("cancel")}>
            Cancel
        </Button>
        <Button bind:disabled on:click={submitForm}>Save</Button>
    </div>
</Modal>

<style>
    form {
        width: 100%;
    }
</style>
