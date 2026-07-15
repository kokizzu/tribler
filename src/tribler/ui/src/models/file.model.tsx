// For compile-time type checking and code completion

import {CheckedState} from "@radix-ui/react-checkbox";

export interface File {
    index: number;
    name: string;
    size: number;
    included: boolean;
    priority: number;
    progress: number;
}

export interface FileTreeItem {
    index: number;
    name: string;
    size: number;
    downloaded?: number;
    progress?: number;
    included?: CheckedState;
    priority?: number;
    subRows?: FileTreeItem[];
}

export interface FileLink {
    uri: string;
    name: string;
}
