export type Player<T> = {
    id: number;
    playerName: string;
    teamName: string;
    score: number;
}

export type Commentator<T> = {
    id: number;
    commentatorName: string;
    xHandle: string;
    teamName: string;
}