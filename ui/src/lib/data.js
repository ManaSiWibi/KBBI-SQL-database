const base = `${import.meta.env.BASE_URL}data/`
const cache = new Map()

async function load(path) {
  if (!cache.has(path)) {
    cache.set(path, fetch(`${base}${path}`).then((response) => {
      if (!response.ok) throw new Error(`Data gagal dimuat (${response.status})`)
      return response.json()
    }).catch((error) => {
      cache.delete(path)
      throw error
    }))
  }
  return cache.get(path)
}

export const getManifest = () => load('manifest.json')
export const getDictionaryIndex = () => load('dictionary-index.json')
export const getDictionaryShard = (letter) => load(`dictionary/${letter}.json`)
export const getBakuNonbaku = () => load('baku-nonbaku.json')
export const getSinonim = () => load('sinonim.json')
export const getAntonim = () => load('antonim.json')

export function normalize(value) {
  return String(value ?? '').trim().toLocaleLowerCase('id-ID')
}

export function definitionToText(value) {
  if (!value) return ''
  const textarea = document.createElement('textarea')
  textarea.innerHTML = value
  const parser = new DOMParser()
  return parser.parseFromString(textarea.value, 'text/html').body.textContent?.trim() ?? ''
}

export function formatNumber(value) {
  return new Intl.NumberFormat('id-ID').format(value ?? 0)
}
