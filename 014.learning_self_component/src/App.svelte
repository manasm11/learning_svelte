<script>
	import Node from "./Node.svelte";

	let directory_structure = {
		root: [
			{ dir1: [{ subdir11: [{ subsubdir1: [] }, { subdir12: [] }] }] },
			{ dir2: [{ subdir21: [] }] },
		],
	};
</script>

{#each directory_structure as member}
	<Node {member} />
{/each}
