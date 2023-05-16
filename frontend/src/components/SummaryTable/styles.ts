import { styled } from "styled-components";


export const Container = styled.div`
  width: 100%;
  display: flex;
`

export const Week = styled.div`
  display: grid;
  grid-auto-flow: row;
  gap: 0.75rem;
  grid-template-rows: repeat(7, minmax(0, 1fr));
`
export const WeekDayName = styled.div`
  color: #A1A1AA;
  font-size: 1.25rem;
  font-weight: 700;
  height: 2.5rem;
  width: 2.5rem;

  display: flex;
  align-items: center;
  justify-content: center;
`

export const Heatmap = styled.div`
  display: grid;
  grid-auto-flow: column;
  grid-template-rows: repeat(7, minmax(0, 1fr));
  gap: 0.75rem
`

export const DayToFill = styled.div`
  height: 2.5rem;
  width: 2.5rem;

  background-color: #18181B;
  border-width: 2px;
  border-color: #27272A;
  border-radius: 0.5rem;

  opacity: 0.4;
  cursor: not-allowed;
`