
<script>
    import {beforeUpdate, onMount} from 'svelte'
    export let name;
    export let type = "text";
    export let required = false;
    let _required = false;
    let _touched = false;

    $:_required = required && _touched

    onMount(()=>{
        i = areValid.length
        areValid.push(false)
    })

</script>

<label>
    <b>{name}</b>
    <input
        {type}
        on:blur={() => (_touched = true)}
        required={_required}
    />
</label>

<style>
    :invalid {
        background-color: rgb(255, 234, 234);
        border: red solid 1px;
    }
</style>
