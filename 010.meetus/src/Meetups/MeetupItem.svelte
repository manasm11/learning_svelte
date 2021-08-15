<script>
    // IMPORTS
    import Button from "../UI/Button.svelte";
    import { createEventDispatcher } from "svelte";
    import Badge from "../UI/Badge.svelte";
    import meetups from "./meetups-store";
    const dispatch = createEventDispatcher();

    // PROPS
    export let id;
    export let title = "--no-title-provided--";
    export let subtitle = "--no-subtitle-provided--";
    export let description = "--no-description-provided--";
    export let imageUrl = "--no-imageUrl-provided--";
    export let address = "--no-address-provided--";
    export let contactEmail = "--no-contactEmail-provided--";
    contactEmail;
    export let isFavorite = false;
</script>

<article>
    <header>
        <h1>
            {title}
            {#if isFavorite}
                <Badge text="FAVOURITE" />
            {/if}
        </h1>
        <h2>{subtitle}</h2>
        <p>{address}</p>
    </header>
    <div class="image">
        <img src={imageUrl} alt={subtitle} />
    </div>
    <div class="content">
        <p>{description}</p>
    </div>
    <footer>
        <Button on:click={() => dispatch("edit", { id })}>Edit</Button>
        <Button
            on:click={() => meetups.toggleFavourite(id)}
            mode="outline {isFavorite || 'success'}"
            >{isFavorite ? "Unfavourite" : "Favourite"}</Button
        >
        <Button on:click={() => dispatch("showdetail", { id })}
            >Show Details</Button
        >
    </footer>
</article>

<style>
    article {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
        border-radius: 5px;
        background: white;
        margin: 1rem;
    }

    header,
    .content,
    footer {
        padding: 1rem;
    }

    .content {
        height: 4rem;
    }

    .image {
        width: 100%;
        height: 14rem;
    }

    .image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border: none;
        outline: none;
    }

    h1 {
        font-size: 1.25rem;
        margin: 0.5rem 0;
        font-family: "Roboto Slab", "sans-sarif";
    }

    /* h1.is-favorite {
        background: #01a129;
        color: white;
        padding: 0 0.5rem;
        border-radius: 5px;
    } */

    h2 {
        font-size: 1rem;
        color: #808080;
        margin: 0.5rem 0;
    }

    p {
        font-size: 1.25rem;
        margin: 0;
    }

    div {
        text-align: right;
    }

    .content {
        height: 4rem;
    }
</style>
