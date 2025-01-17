export type ProfesorDB = {
        "id" : string
        "name": string
        "fullname": string
        "specialty": string
        "contract_type": string
        "experience": number
        "email": string
        "username": string
        "list_of_subjects": string[]
        "valoration": string
    }

export type ProfesorGetResponse = {
    [index: string]: ProfesorDB
}