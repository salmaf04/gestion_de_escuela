export type MantenimientoGetDB = {
    id : string;
    mean_id: string;
    date_id: string;
    cost: number;
};

export type MantenimientoGetResponse = {
    [index: string]: MantenimientoGetDB
}