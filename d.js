
function formatDate() {
    const date = new Date()
    return date.toISOString().split("T")[0]
}

console.log(formatDate())

