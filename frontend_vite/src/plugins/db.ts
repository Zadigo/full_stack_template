const isIndexedDBSupported = typeof window !== 'undefined' && 'indexedDB' in window && window.indexedDB !== null

export default function useIndexDatabase () {
    async function createConnection (name: string) {
        return new Promise<IDBDatabase>((resolve, reject) => {
            try {
                if (isIndexedDBSupported) {
                    const request = indexedDB.open(name)
                    
                    request.onsuccess = () => {
                        return resolve(request.result)
                    }
    
                    request.onerror = () => {
                        return reject(request.error)
                    }
    
                    /**
                     * The upgradeneeded event is fired when an attempt 
                     * was made to open a database with a version number 
                     * higher than its current version
                     */
                    request.onupgradeneeded = (_e) => {
                        const db = request.result
    
                        if (!db.objectStoreNames.contains('storage')) {
                            db.createObjectStore('storage')
                        }
                    }
                } else {
                    reject('IndexDB is not supported')
                }
            } catch (error) {
                reject(error)
            }
        })
    }

    return {
        createConnection
    }
}
