export interface CreateNewHabitRequest {
  title: string;
  startAt: string;
}

export interface ListHabitsRequest {
  date?: string
}

export interface CheckHabitRequest {
  habit: string;
  date: string;

}