// Attenzione: questo script potrebbe causare instabilità se la RAM ha problemi
// Test di allocazione memoria semplice
function testMemoryAllocation() {
  console.log("Iniziando test di allocazione memoria...");
  
  const memArrays = [];
  const bytesPerArray = 100 * 1024 * 1024; // ~100MB per array
  const targetGB = 16; // Quanti GB vuoi testare
  const arrayCount = (targetGB * 1024) / (bytesPerArray / 1024 / 1024);
  
  try {
    console.log(`Tentativo di allocare circa ${targetGB}GB di memoria...`);
    
    for (let i = 0; i < arrayCount; i++) {
      // Crea array di circa 100MB
      const arr = new Uint8Array(bytesPerArray);
      
      // Scrivi e leggi per verificare
      for (let j = 0; j < arr.length; j += 1024) {
        arr[j] = j % 256;
      }
      
      // Verifica la scrittura
      for (let j = 0; j < arr.length; j += 1024) {
        if (arr[j] !== j % 256) {
          throw new Error(`Errore di verifica alla posizione ${j}`);
        }
      }
      
      memArrays.push(arr);
      console.log(`Allocati ${(i+1) * (bytesPerArray / 1024 / 1024 / 1024).toFixed(2)}GB`);
    }
    
    console.log("Test completato con successo!");
  } catch (error) {
    console.error("Errore durante il test:", error);
  }
}

testMemoryAllocation();