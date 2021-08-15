<script>
    import Button from "../UI/Button.svelte";
    import meetups from "./meetups-store";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    export let id;

    let { title, subtitle, description, contactEmail, address, imageUrl } =
        $meetups.find((m) => m.id == id);
</script>

<section>
    <div class="image">
        <img src={imageUrl} alt="" />
    </div>
    <div class="content">
        <h1>{title}</h1>
        <h2>{subtitle} - {address}</h2>
        <p>{description}</p>
        <Button><a href="mailto:{contactEmail}">Contact</a></Button>
        <Button on:click={() => dispatch("closedetail")}>Close</Button>
    </div>
</section>

<style>
    img {
        height: 25rem;
        width: 100%;
    }

    section {
        margin: 2rem;
    }
</style>
