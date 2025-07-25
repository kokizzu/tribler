import * as React from "react";
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area";

import {cn} from "@/lib/utils";

const ScrollArea = React.forwardRef<
    React.ElementRef<typeof ScrollAreaPrimitive.Root>,
    React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.Root>
>(({className, children, ...props}, ref) => (
    <ScrollAreaPrimitive.Root className={cn("relative overflow-hidden", className)} {...props}>
        <ScrollAreaPrimitive.Viewport ref={ref} className="h-full w-full rounded-[inherit]">
            {children}
        </ScrollAreaPrimitive.Viewport>
        <ScrollBar />
        <ScrollAreaPrimitive.Corner />
    </ScrollAreaPrimitive.Root>
));
ScrollArea.displayName = ScrollAreaPrimitive.Root.displayName;

const ScrollBar = React.forwardRef<
    React.ElementRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>,
    React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>
>(({className, orientation = "vertical", ...props}, ref) => (
    <ScrollAreaPrimitive.ScrollAreaScrollbar
        ref={ref}
        orientation={orientation}
        className={cn(
            "flex touch-none select-none transition-colors z-50",
            orientation === "vertical" && "h-full w-2.5 border-l border-l-transparent p-[1px]",
            orientation === "horizontal" && "h-2.5 border-t border-t-transparent p-[1px]",
            className
        )}
        {...props}>
        <ScrollAreaPrimitive.ScrollAreaThumb
            className={cn("relative rounded-full bg-primary", orientation === "vertical" && "flex-1")}
        />
    </ScrollAreaPrimitive.ScrollAreaScrollbar>
));
ScrollBar.displayName = ScrollAreaPrimitive.ScrollAreaScrollbar.displayName;

export {ScrollArea, ScrollBar};
