import {EndpointEnum} from "./EndpointEnum.ts";
import {IApiObject} from "./IApiObject.ts";


function postApi(endpoint: EndpointEnum, body: IApiObject) {
    return fetch(`http://localhost:8000/${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(body),
    })
}

function getApi(endpoint: EndpointEnum) {
    return fetch(`http://localhost:8000/${endpoint}`, {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}
function getOneApi(endpoint: EndpointEnum, id: string) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}
//todo id path everybody
function patchApi(endpoint: EndpointEnum, id: string = "", body: IApiObject) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
        },
        body: JSON.stringify(body),
    })
}

function deleteApi(endpoint: EndpointEnum, id: string) {
    return fetch(`http://localhost:8000/${endpoint}/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        }
    })
}

export default {getApi, postApi, deleteApi, patchApi, getOneApi}