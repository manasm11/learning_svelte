<script>
    // IMPORTS
    import { onMount, createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    // VAARIABLES
    let name = "";
    let firstInput = "";
    $: disabled = !name;
    let active = false;

    // ONMOUNT
    onMount(() => {
        firstInput.focus();
        active = true;
    });

    // FUNCTIONS
    function fnResetDisabled() {
        name = "";
        firstInput.focus();
    }
</script>

<form>
    <label>
        Name
        <input
            type="text"
            class:active
            placeholder="Enter your name"
            on:focus={() => (active = true)}
            on:blur={() => (active = false)}
            bind:value={name}
            bind:this={firstInput}
        />
    </label>
    <article>
        <button type="reset" {disabled} on:click={fnResetDisabled}>Reset</button
        >
        <button on:click|preventDefault={() => dispatch("createQRCode", name)}
            >Create QR Code</button
        >
    </article>
</form>

<style>
    input:focus {
        outline: none;
    }
    input.active {
        border-color: hsl(211, 63%, 35%);
        box-shadow: hsla(211, 63%, 35%, 0.5);
    }
    label {
        display: flex;
        align-items: baseline;
        margin: 0.5rem;
        font-weight: bold;
    }
    input {
        width: 100%;
        margin: 0 0.5rem;
        border-radius: 5px;
    }
    article {
        display: flex;
        justify-content: space-evenly;
    }
    button {
        margin: 0.5rem;
        cursor: pointer;
        border-radius: 5px;
    }
</style>
