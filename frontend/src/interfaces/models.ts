export interface Habit {
  id: number;
  name: string;
  start_at: string
}

export interface Day{
  id: number;
  date: string;
  completed: number;
  total: number;
}