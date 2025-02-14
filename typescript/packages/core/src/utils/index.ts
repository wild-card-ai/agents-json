/**
 * Converts dot notation with digits to bracket notation for array access
 * e.g., "items.0.name" becomes "items[0].name"
 */
export function convertDotDigitsToBrackets(path: string): string {
  return path.replace(/\.(\d+)(?=\.|$)/g, '[$1]');
}

/**
 * Deep merge two objects
 */
export function deepMerge<T extends Record<string, any>>(target: T, source: Partial<T>): T {
  const output = { ...target };
  
  for (const key in source) {
    if (source.hasOwnProperty(key)) {
      if (isObject(source[key]) && isObject(target[key])) {
        output[key] = deepMerge(target[key], source[key]);
      } else {
        output[key] = source[key] as any;
      }
    }
  }
  
  return output;
}

/**
 * Type guard for objects
 */
function isObject(item: any): item is Record<string, any> {
  return item && typeof item === 'object' && !Array.isArray(item);
}

/**
 * Get a value from an object using dot notation
 */
export function get(obj: any, path: string): any {
  const normalizedPath = convertDotDigitsToBrackets(path);
  const keys = normalizedPath.split(/[.[\]]+/).filter(Boolean);
  
  return keys.reduce((acc, key) => {
    if (acc === null || acc === undefined) return undefined;
    return acc[key];
  }, obj);
}

/**
 * Set a value in an object using dot notation
 */
export function set(obj: any, path: string, value: any): void {
  const normalizedPath = convertDotDigitsToBrackets(path);
  const keys = normalizedPath.split(/[.[\]]+/).filter(Boolean);
  
  let current = obj;
  for (let i = 0; i < keys.length - 1; i++) {
    const key = keys[i];
    if (!(key in current)) {
      // If next key is a number, create an array, otherwise an object
      current[key] = /^\d+$/.test(keys[i + 1]) ? [] : {};
    }
    current = current[key];
  }
  
  const lastKey = keys[keys.length - 1];
  current[lastKey] = value;
}
