<script>
	import {count} from './stores'
</script>

<h1>Count: {$count}</h1>
<button on:click={() => $count++}>INCREMENT</button>
<button on:click={() => $count=0}>RESET</button>