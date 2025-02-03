export type MedioGetDB = {
    id : string;
    name: string;
    state: string;
    location: string;
    classroom_id: string;
    type: string;
    to_be_replaced: boolean
};

export type MedioGetResponse = {
    [index: string]: MedioGetDB
}