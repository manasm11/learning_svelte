export default Intl.DateTimeFormat("en", {
    hour12: true,
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
}
).format