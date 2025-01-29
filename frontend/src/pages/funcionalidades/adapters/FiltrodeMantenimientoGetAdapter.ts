
export class FiltrodeMantenimientoGetAdapter {
    classroom_id: string;
    other: number;
    teaching_material: number;
    technological_mean: number;
    total_maintenances_after_two_years: number;

    constructor(classroom: { classroom_id: string, other: number, teaching_material: number, technological_mean: number }, summary: { "total maintenances after two years": number }) {
        this.classroom_id = classroom.classroom_id;
        this.other = classroom.other;
        this.teaching_material = classroom.teaching_material;
        this.technological_mean = classroom.technological_mean;
        this.total_maintenances_after_two_years = summary["total maintenances after two years"];
    }
    [key: string]: string | number;
}