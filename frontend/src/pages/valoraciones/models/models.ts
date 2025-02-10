export type ValoracionPorAsignaturaDeProfesorGetDB = {
    id: string;
    teacher: {
        id: string;
        name: string;
        lastname: string;
        specialty: string;
        contract_type: string;
        experience: number;
        email: string;
        username: string;
        salary: number;
        subjects: {
            id: string;
            name: string;
            hourly_load: number;
            study_program: number;
            classroom: {
                number: number;
                location: string;
                capacity: number;
                id: string;
            };
            course: {
                year: number;
                id: string;
            };
        }[];
        valoration: number;
        alert: number;
    };
    subject: {
        id: string;
        name: string;
        hourly_load: number;
        study_program: number;
        classroom: {
            number: number;
            location: string;
            capacity: number;
            id: string;
        };
        course: {
            year: number;
            id: string;
        };
    };
    course: {
        year: number;
        id: string;
    };
    grade: number;
};