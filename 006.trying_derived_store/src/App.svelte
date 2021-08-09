<script>
	import { time, elapsed } from "./derived_store";
	import formatter from './date_formatter'
</script>

<h1>Time: {formatter($time)}</h1>
<h2>Time elapsed: {$elapsed}</h2>