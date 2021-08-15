<script>
    export let type;
    export let value;
    export let validators;
    export let valid = false;
    $: valid = isValid && touched;
    let isValid = true;

    let touched = false || type === "id";

    $: {
        for (let i = 0; i < validators.length; i++) {
            if (!touched) {
                isValid = true;
                break;
            }
            if (!validators[i](value)) {
                isValid = false;
                break;
            }
            isValid = true;
        }
    }

    const label = {
        title: "Title",
        subtitle: "Subtitle",
        address: "Address",
        imageUrl: "Image URL",
        contactEmail: "Email",
        id: "",
        isFavorite: "",
        description: "Description",
    };
</script>

{#if type !== "id" && type !== "isFavorite"}
    <div class="form-control">
        <label for={type}>{label[type]}</label>
        {#if type === "description"}
            <textarea
                id={type}
                rows="3"
                on:blur={() => (touched = true)}
                class:invalid={!isValid}
                bind:value
            />
        {:else if type === "contactEmail"}
            <input
                type="email"
                class:invalid={!isValid}
                on:blur={() => (touched = true)}
                id={type}
                bind:value
            />
        {:else}
            <input
                type="text"
                on:blur={() => (touched = true)}
                class:invalid={!isValid}
                id={type}
                bind:value
            />
        {/if}
        {#if !isValid}
            <invalid-message> Invalid </invalid-message>
        {/if}
    </div>
{/if}

<style>
    .invalid {
        border-color: red;
        background-color: rgb(255, 240, 240);
    }

    invalid-message {
        color: red;
        font-size: 0.9rem;
    }

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
