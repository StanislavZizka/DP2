// Language Switcher System
class LanguageSwitcher {
    constructor() {
        this.currentLanguage = localStorage.getItem('selectedLanguage') || 'cs';
        this.translations = {
            cs: {
                // Navigation
                'nav-home': 'Domov',
                'nav-activator-inhibitor': 'Aktivátor-Inhibitor',
                'nav-waves': 'Oscilační vlny',
                'nav-stripes': 'Zebří pruhy',
                
                // Home page
                'page-title-home': 'Generátor Matematických Textur',
                'page-subtitle-home': 'Vytvářejte úžasné vzory pomocí matematických modelů',
                'home-description': 'Objevte sílu matematiky v umění. Naše aplikace využívá pokročilé algoritmy pro generování nádherných textur a vzorů, které můžete aplikovat na 3D modely.',
                'features-title': 'Funkce aplikace',
                'feature-1-title': 'Reakčně-difuzní modely',
                'feature-1-desc': 'Generujte komplexní vzory pomocí aktivátor-inhibitor modelů',
                'feature-2-title': '3D Vizualizace',
                'feature-2-desc': 'Vytvářejte vlnové vzory s různými frekvencemi',
                'feature-3-title': 'Interaktivní rozhraní',
                'feature-3-desc': 'Generujte pruhované textury s nastavitelnými parametry',
                'feature-4-title': 'Export a stažení',
                'feature-4-desc': 'Uložte si vygenerované textury ve vysoké kvalitě',
                'get-started': 'Začít vytvářet',
                
                // Activator-Inhibitor page
                'page-title-ai': 'Aktivátor-Inhibitor Model',
                'page-subtitle-ai': 'Nastavte parametry reakčně-difuzního modelu pro generování komplexních vzorů a textur',
                'model-params': 'Parametry modelu',
                'constant-k': 'Konstanta K',
                'constant-k-help': 'Rychlost reakčního procesu (0.1 - 5.0)',
                'max-time': 'Maximální čas',
                'max-time-help': 'Doba simulace v časových jednotkách',
                'time-step': 'Časový krok',
                'time-step-help': 'Přesnost simulačního kroku',
                'color-scheme': 'Barevné schéma',
                'base-color': 'Základní barva',
                'contrast-color': 'Kontrastní barva',
                'generate-texture': 'Generovat texturu',
                'result-texture': 'Výsledná textura',
                'placeholder-text': 'Zde se zobrazí vygenerovaná textura',
                'download': 'Stáhnout',
                'view': 'Zobrazit',
                'generating': 'Generuji texturu...',
                
                // 3D Visualization
                '3d-visualization': '3D Vizualizace',
                'select-shell-type': 'Vyberte typ mušle:',
                'shell-buccinidae': 'Buccinidae (Hornovec)',
                'shell-fasciolariidae': 'Fasciolariidae (Fasciolarievité)',
                'shell-moon-snail': 'Moon snail (Měsíční šnek)',
                'shell-muricidae': 'Muricidae (Murexovité)',
                'shell-pecten': 'Pecten (Hřebnatka)',
                'shell-whelk': 'Whelk (Růžek)',
                'loading-model': 'Načítám 3D model...',
                'instruction-drag': 'Přetáhněte texturu na mušli pro aplikaci',
                'instruction-mouse': 'Levé tlačítko: otáčení • Kolečko myši: zoom in/out',
                'instruction-mobile': 'Mobil: 1 prst = otáčení • 2 prsty = pinch zoom',
                'reset-texture': 'Resetovat texturu',
                'change-model': 'Změnit model',
                
                // Popup controls
                'popup-close-info': 'ESC / Kliknutí mimo / Swipe dolů pro zavření',
                'popup-zoom-info': 'Dvojklik pro zoom • Pinch pro zoom na mobilu',
                
                // Toast messages
                'texture-generated': 'Textura byla úspěšně vygenerována!',
                'texture-applied': 'Textura byla úspěšně aplikována na mušli!',
                'texture-reset': 'Textura byla resetována na původní barvy!',
                'model-loading': 'Načítám model:',
                'texture-generation-error': 'Chyba při generování textury',
                'server-error': 'Chyba při komunikaci se serverem',
                'model-not-ready': 'Model není připraven pro aplikaci textury',
                'enter-valid-values': 'Zadejte platné hodnoty pro všechny parametry',
                'fallback-model': 'Použit náhradní model',
                
                // Language switcher
                'language': 'Jazyk',
                'czech': 'Čeština',
                'english': 'Angličtina',
                'language-switched': 'Jazyk byl změněn',
                
                // Theme toggle
                'theme-dark': 'Tmavý',
                'theme-light': 'Světlý',
                'switch-to-light': 'Přepnout na světlý režim',
                'switch-to-dark': 'Přepnout na tmavý režim',
                
                // Common buttons
                'coming-soon': 'Brzy k dispozici'
            },
            en: {
                // Navigation
                'nav-home': 'Home',
                'nav-activator-inhibitor': 'Activator-Inhibitor',
                'nav-waves': 'Oscillating Waves',
                'nav-stripes': 'Zebra Stripes',
                
                // Home page
                'page-title-home': 'Mathematical Texture Generator',
                'page-subtitle-home': 'Create amazing patterns using mathematical models',
                'home-description': 'Discover the power of mathematics in art. Our application uses advanced algorithms to generate beautiful textures and patterns that you can apply to 3D models.',
                'features-title': 'Application Features',
                'feature-1-title': 'Reaction-Diffusion Models',
                'feature-1-desc': 'Generate complex patterns using activator-inhibitor models',
                'feature-2-title': '3D Visualization',
                'feature-2-desc': 'Create wave patterns with various frequencies',
                'feature-3-title': 'Interactive Interface', 
                'feature-3-desc': 'Generate striped textures with configurable parameters',
                'feature-4-title': 'Export and Download',
                'feature-4-desc': 'Save generated textures in high quality',
                'get-started': 'Start Creating',
                
                // Activator-Inhibitor page
                'page-title-ai': 'Activator-Inhibitor Model',
                'page-subtitle-ai': 'Set parameters for the reaction-diffusion model to generate complex patterns and textures',
                'model-params': 'Model Parameters',
                'constant-k': 'Constant K',
                'constant-k-help': 'Reaction process rate (0.1 - 5.0)',
                'max-time': 'Maximum Time',
                'max-time-help': 'Simulation duration in time units',
                'time-step': 'Time Step',
                'time-step-help': 'Simulation step precision',
                'color-scheme': 'Color Scheme',
                'base-color': 'Base Color',
                'contrast-color': 'Contrast Color',
                'generate-texture': 'Generate Texture',
                'result-texture': 'Result Texture',
                'placeholder-text': 'Generated texture will appear here',
                'download': 'Download',
                'view': 'View',
                'generating': 'Generating texture...',
                
                // 3D Visualization
                '3d-visualization': '3D Visualization',
                'select-shell-type': 'Select shell type:',
                'shell-buccinidae': 'Buccinidae (Whelk)',
                'shell-fasciolariidae': 'Fasciolariidae (Tulip Shell)',
                'shell-moon-snail': 'Moon snail',
                'shell-muricidae': 'Muricidae (Murex)',
                'shell-pecten': 'Pecten (Scallop)',
                'shell-whelk': 'Whelk',
                'loading-model': 'Loading 3D model...',
                'instruction-drag': 'Drag texture onto shell to apply',
                'instruction-mouse': 'Left click: rotate • Mouse wheel: zoom in/out',
                'instruction-mobile': 'Mobile: 1 finger = rotate • 2 fingers = pinch zoom',
                'reset-texture': 'Reset Texture',
                'change-model': 'Change Model',
                
                // Popup controls
                'popup-close-info': 'ESC / Click outside / Swipe down to close',
                'popup-zoom-info': 'Double click to zoom • Pinch to zoom on mobile',
                
                // Toast messages
                'texture-generated': 'Texture generated successfully!',
                'texture-applied': 'Texture applied successfully to shell!',
                'texture-reset': 'Texture reset to original colors!',
                'model-loading': 'Loading model:',
                'texture-generation-error': 'Error generating texture',
                'server-error': 'Server communication error',
                'model-not-ready': 'Model not ready for texture application',
                'enter-valid-values': 'Enter valid values for all parameters',
                'fallback-model': 'Using fallback model',
                
                // Language switcher
                'language': 'Language',
                'czech': 'Czech',
                'english': 'English',
                'language-switched': 'Language switched',
                
                // Theme toggle
                'theme-dark': 'Dark',
                'theme-light': 'Light',
                'switch-to-light': 'Switch to light mode',
                'switch-to-dark': 'Switch to dark mode',
                
                // Common buttons
                'coming-soon': 'Coming Soon'
            }
        };
        
        this.init();
    }

    init() {
        this.createLanguageSwitcher();
        this.applyLanguage(this.currentLanguage);
        this.setupEventListeners();
    }

    createLanguageSwitcher() {
        // Create language switcher HTML
        const languageSwitcher = document.createElement('div');
        languageSwitcher.className = 'language-switcher';
        languageSwitcher.innerHTML = `
            <div class="language-toggle" id="languageToggle">
                <div class="language-option ${this.currentLanguage === 'cs' ? 'active' : ''}" data-lang="cs">
                    <span class="flag">🇨🇿</span>
                    <span class="lang-name" data-i18n="czech">Čeština</span>
                </div>
                <div class="language-option ${this.currentLanguage === 'en' ? 'active' : ''}" data-lang="en">
                    <span class="flag">🇺🇸</span>
                    <span class="lang-name" data-i18n="english">English</span>
                </div>
            </div>
        `;

        // Insert after theme toggle
        const themeToggle = document.querySelector('.theme-toggle');
        if (themeToggle && themeToggle.parentNode) {
            themeToggle.parentNode.insertBefore(languageSwitcher, themeToggle.nextSibling);
        } else {
            // Fallback: add to body
            document.body.appendChild(languageSwitcher);
        }
    }

    setupEventListeners() {
        const languageOptions = document.querySelectorAll('.language-option');
        languageOptions.forEach(option => {
            option.addEventListener('click', (e) => {
                const selectedLang = e.currentTarget.getAttribute('data-lang');
                this.switchLanguage(selectedLang);
            });
        });
    }

    switchLanguage(language) {
        if (language !== this.currentLanguage && this.translations[language]) {
            this.currentLanguage = language;
            localStorage.setItem('selectedLanguage', language);
            
            // Update active state
            document.querySelectorAll('.language-option').forEach(option => {
                option.classList.remove('active');
            });
            document.querySelector(`[data-lang="${language}"]`).classList.add('active');
            
            this.applyLanguage(language);
            
            // Update theme toggle button if it exists
            if (window.themeManager && window.themeManager.updateToggleButton) {
                window.themeManager.updateToggleButton();
            }
            
            this.showToast(this.getTranslation('language-switched', language));
        }
    }

    applyLanguage(language) {
        const elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(element => {
            const key = element.getAttribute('data-i18n');
            const translation = this.getTranslation(key, language);
            
            if (translation) {
                if (element.tagName === 'INPUT' && element.type === 'submit') {
                    element.value = translation;
                } else if (element.hasAttribute('placeholder')) {
                    element.placeholder = translation;
                } else if (element.hasAttribute('aria-label')) {
                    element.setAttribute('aria-label', translation);
                } else if (element.tagName === 'OPTION') {
                    element.textContent = translation;
                } else {
                    element.textContent = translation;
                }
            }
        });

        // Update document language attribute
        document.documentElement.setAttribute('lang', language);
    }

    getTranslation(key, language = null) {
        const lang = language || this.currentLanguage;
        return this.translations[lang] && this.translations[lang][key] 
            ? this.translations[lang][key] 
            : this.translations['cs'][key] || key;
    }

    showToast(message, type = 'info') {
        // Use existing toast system if available
        if (typeof showToast === 'function') {
            showToast(message, type);
        } else {
            console.log('Language switched:', message);
        }
    }

    // Global method to get current language
    getCurrentLanguage() {
        return this.currentLanguage;
    }

    // Global method to translate text dynamically
    t(key) {
        return this.getTranslation(key);
    }
}

// Initialize language switcher when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.languageSwitcher = new LanguageSwitcher();
    
    // Make translation function globally available
    window.t = (key) => window.languageSwitcher.t(key);
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LanguageSwitcher;
}