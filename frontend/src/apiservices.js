const API_BASE_URL ="http://127.0.0.1:5000"

async function request(endpoint, options = {}) {
    const token = localStorage.getItem("token");
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
    };

    if (token) {
        headers['Authentication-Token'] = token;
    }

    const config = {
        ...options,
        headers,
    };

    const response = await fetch(`${API_BASE_URL}${endpoint}`, config);

    if (response.status === 401) {
        // Handle unauthorized access globally, e.g., redirect to login
        window.location.href = '/login'; 
        throw new Error('Unauthorized');
    }

    if (!response.ok) {
        // Handle other errors
        const errorData = await response.json();
        throw new Error(errorData.message || 'Something went wrong');
    }

    // For DELETE requests which might not have a body
    if (response.status === 204 || response.headers.get("content-length") === "0") {
        return {}; 
    }

    return response.json();
}

export const subjectService = {
    getAll: () => request('/api/subjects'),
    create: (data) => request('/api/subjects', { method: 'POST', body: JSON.stringify(data) }),
    update: (id, data) => request(`/api/subjects?id=${id}`, { method: 'PUT', body: JSON.stringify(data) }),
    delete: (id) => request(`/api/subjects?id=${id}`, { method: 'DELETE' }),
};
export const chapterService  = {
    getAll: () => request('/api/chapters' , {method:"GET"}),
    create: (data) => request('/api/chapters', { method: 'POST', body: JSON.stringify(data) }),
    update: (id, data) => request(`/api/chapters?id=${id}`, { method: 'PUT', body: JSON.stringify(data) }),
    delete: (id) => request(`/api/chapterss?id=${id}`, { method: 'DELETE' }),
};



