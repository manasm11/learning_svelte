<script>
    export let type;
    export let value;
    const label = {
        title: "Title",
        subtitle: "Subtitle",
        address: "Address",
        imageUrl: "Image URL",
        contactEmail: "Email",
        id: '',
        description: "Description",
    };
</script>

<div class="form-control">
    <label for={type}>{label[type]}</label>
    {#if type === "description"}
        <textarea id={type} rows="3" bind:value />
    {:else if type === "contactEmail"}
        <input type="email" id={type} bind:value />
    {:else if type === "id"}
        <div style="display: none;"></div>
    {:else}
        <input type="text" id={type} bind:value />
    {/if}
</div>


<style>

    input,
    textarea {
        display: block;
        width: 100%;
        font: inherit;
        border: none;
        border-bottom: 2px solid #ccc;
        border-radius: 3px 3px 0 0;
        background: white;
        padding: 0.15rem 0.25rem;
        transition: border-color 0.1s ease-out;
        resize: none;
        overflow: hidden;
    }

    input:focus,
    textarea:focus {
        border-color: #e40763;
        outline: none;
    }

    label {
        display: block;
        margin-bottom: 0.5rem;
        width: 100%;
    }

    .form-control {
        padding: 0.5rem 0;
        width: 100%;
        margin: 0.25rem 0;
    }
</style>
