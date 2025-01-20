function getToken(username: string, password: string) {
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    return fetch('http://localhost:8000/token/', {
        method: 'POST',
        body: formData,
    })
}
export default {
    getToken
}