export type AulaGetDB = {
    id : string ;
    location: string;
    capacity: number;
    number: number
};

export type AulaGetResponse = {
    [index: string]: AulaGetDB
}