
export type EstudianteGetDB = {
    "id" : string
    "name": "string",
    "age": number,
    "email": "string",
    "extra_activities": boolean,
    "username": "string",
    "password": "string"
}

export type EstudianteGetResponse = {
    [index: string]: EstudianteGetDB
}