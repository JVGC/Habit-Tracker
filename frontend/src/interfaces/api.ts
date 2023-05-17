export interface CreateNewHabitRequest {
  title: string;
  startAt: string;
}

export interface ListHabitsRequest {
  date?: string
}