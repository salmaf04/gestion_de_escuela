import {EndpointType} from "./EndpointType.ts";
import {IApiObject} from "./IApiObject.ts";


function postApi(endpoint: EndpointType, body: IApiObject) {
    return fetch(`http://localhost:8000/${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(body),
    })
}

function getApi(endpoint: EndpointType) {
    return fetch(`http://localhost:8000/${endpoint}`, {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}
function getOneApi(endpoint: EndpointType, id: string) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

function patchApi(endpoint: EndpointType, id: string, body: IApiObject) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(body),
    })
}

function deleteApi(endpoint: EndpointType, id: string) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {getApi, postApi, deleteApi, patchApi, getOneApi}