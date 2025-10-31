// THE LAST SCROLL - Main JavaScript
// Digital mortality simulator

class DigitalApocalypse {
    constructor() {
        this.memories = [];
        this.loadedMemories = [];
        this.currentIndex = 0;
        this.savesRemaining = 15;
        this.savedMemories = [];
        this.internetIntegrity = 100;
        this.timeRemaining = 600; // 10 minutes in seconds
        this.isEnded = false;
        this.scrollResistance = 1;
        this.ghostUsers = [];
        this.ghostActivityTimer = null;
        
        this.init();
    }

    async init() {
        await this.loadMemories();
        this.setupEventListeners();
        this.startApocalypse();
        this.loadInitialMemories();
        this.initializeGhostUsers();
        this.startGhostActivity();
    }

    async loadMemories() {
        try {
            const response = await fetch('memories.json');
            this.memories = await response.json();
            console.log(`Loaded ${this.memories.length} memories`);
        } catch (error) {
            console.error('Failed to load memories:', error);
            // Fallback memories if JSON fails
            this.memories = this.getFallbackMemories();
        }
    }

    getFallbackMemories() {
        return [
            {
                id: 1,
                type: "tweet",
                content: "The internet is dying and we're all just scrolling through its death throes...",
                author: "digital_mourner",
                year: 2024,
                corruptionLevel: 0,
                saved: false
            }
        ];
    }

    setupEventListeners() {
        window.addEventListener('scroll', this.handleScroll.bind(this));
        window.addEventListener('wheel', this.handleWheel.bind(this));
        
        // Prevent back scrolling - one way journey to digital death
        window.addEventListener('scroll', () => {
            if (window.scrollY < this.lastScrollY) {
                window.scrollTo(0, this.lastScrollY);
            }
            this.lastScrollY = window.scrollY;
        });
        
        this.lastScrollY = 0;
    }

    handleScroll() {
        if (this.isEnded) return;
        
        const scrollPosition = window.scrollY;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        
        // Load more memories as user scrolls
        if (scrollPosition > documentHeight - windowHeight * 2) {
            this.loadMoreMemories();
        }
        
        // Increase corruption based on scroll speed and distance
        this.updateCorruptionBasedOnScroll();
    }

    handleWheel(event) {
        if (this.isEnded) return;
        
        // Add scroll resistance that increases over time
        if (this.scrollResistance > 1) {
            event.preventDefault();
            const scrollAmount = event.deltaY / this.scrollResistance;
            window.scrollBy(0, scrollAmount);
        }
        
        // Faster scrolling = faster corruption
        const scrollSpeed = Math.abs(event.deltaY);
        if (scrollSpeed > 100) {
            this.accelerateCorruption();
        }
    }

    loadInitialMemories() {
        const feed = document.getElementById('feed');
        
        // Load first batch of memories
        for (let i = 0; i < Math.min(10, this.memories.length); i++) {
            this.renderMemory(this.memories[i]);
            this.loadedMemories.push(this.memories[i]);
            this.currentIndex++;
        }
    }

    loadMoreMemories() {
        if (this.currentIndex >= this.memories.length) return;
        
        const feed = document.getElementById('feed');
        const batchSize = 5;
        
        for (let i = 0; i < batchSize && this.currentIndex < this.memories.length; i++) {
            const memory = this.memories[this.currentIndex];
            this.renderMemory(memory);
            this.loadedMemories.push(memory);
            this.currentIndex++;
        }
    }

    renderMemory(memory) {
        const feed = document.getElementById('feed');
        const memoryCard = document.createElement('div');
        memoryCard.className = 'memory-card';
        memoryCard.id = `memory-${memory.id}`;
        
        memoryCard.innerHTML = `
            <div class="memory-header">
                <div class="memory-meta">
                    <span class="memory-type">${memory.type}</span>
                </div>
            </div>
            <div class="memory-content" id="content-${memory.id}">
                ${memory.content}
            </div>
            <div class="memory-footer">
                <div class="memory-info">
                    <span class="memory-author">@${memory.author}</span>
                    <span class="memory-year">${memory.year}</span>
                </div>
                <button 
                    class="save-btn" 
                    onclick="apocalypse.saveMemory(${memory.id})"
                    ${this.savesRemaining <= 0 ? 'disabled' : ''}
                >
                    💾 Save
                </button>
            </div>
        `;
        
        feed.appendChild(memoryCard);
        
        // Add random initial corruption for variety
        if (Math.random() < 0.1) {
            this.addRandomGlitch(memoryCard);
        }
    }

    saveMemory(memoryId) {
        if (this.savesRemaining <= 0 || this.isEnded) return;
        
        const memory = this.memories.find(m => m.id === memoryId);
        if (!memory || memory.saved) return;
        
        memory.saved = true;
        this.savedMemories.push(memory);
        this.savesRemaining--;
        
        // Update UI
        const memoryCard = document.getElementById(`memory-${memoryId}`);
        const saveBtn = memoryCard.querySelector('.save-btn');
        saveBtn.textContent = '✅ Saved';
        saveBtn.className = 'save-btn saved';
        saveBtn.disabled = true;
        
        // Freeze this memory from corruption
        memoryCard.classList.add('saved-memory');
        
        // Update counters
        document.getElementById('saves-remaining').textContent = this.savesRemaining;
        document.getElementById('vault-count').textContent = this.savedMemories.length;
        
        // Disable all save buttons if no saves left
        if (this.savesRemaining <= 0) {
            document.querySelectorAll('.save-btn:not(.saved)').forEach(btn => {
                btn.disabled = true;
                btn.textContent = '❌ No saves left';
            });
        }
        
        // Visual feedback
        this.createSaveEffect(memoryCard);
    }

    createSaveEffect(memoryCard) {
        memoryCard.style.border = '2px solid #27ae60';
        memoryCard.style.background = 'rgba(39, 174, 96, 0.1)';
        
        setTimeout(() => {
            memoryCard.style.border = '1px solid #27ae60';
            memoryCard.style.background = 'rgba(30, 30, 30, 0.9)';
        }, 1000);
    }

    startApocalypse() {
        // Main corruption timer
        this.corruptionTimer = setInterval(() => {
            if (this.isEnded) return;
            
            this.tickCorruption();
            this.updateCountdown();
            this.updateScrollResistance();
            
            // Check end conditions
            if (this.timeRemaining <= 0 || this.internetIntegrity <= 0) {
                this.endWorld();
            }
            
        }, 1000);
        
        // Faster corruption pulses
        this.fastCorruptionTimer = setInterval(() => {
            if (this.isEnded) return;
            this.fastCorruptionTick();
        }, 200);
    }

    tickCorruption() {
        this.internetIntegrity = Math.max(0, this.internetIntegrity - 0.5);
        this.timeRemaining--;
        
        // Update integrity display
        document.getElementById('integrity').textContent = Math.round(this.internetIntegrity) + '%';
        
        // Apply corruption to loaded memories
        this.loadedMemories.forEach(memory => {
            if (!memory.saved && memory.corruptionLevel < 100) {
                this.corruptMemory(memory);
            }
        });
        
        // Increase corruption rate as time runs out
        if (this.timeRemaining < 120) { // Last 2 minutes
            this.accelerateCorruption();
        }
    }

    fastCorruptionTick() {
        // Random glitch effects
        if (Math.random() < 0.1) {
            this.addRandomGlobalGlitch();
        }
        
        // Corrupt random visible memories
        const visibleMemories = this.getVisibleMemories();
        visibleMemories.forEach(memory => {
            if (!memory.saved && Math.random() < 0.05) {
                this.addRandomGlitch(document.getElementById(`memory-${memory.id}`));
            }
        });
    }

    corruptMemory(memory) {
        if (memory.saved) return;
        
        // Increase corruption level
        const corruptionIncrease = 0.5 + (Math.random() * 0.5);
        memory.corruptionLevel = Math.min(100, memory.corruptionLevel + corruptionIncrease);
        
        const memoryCard = document.getElementById(`memory-${memory.id}`);
        if (!memoryCard) return;
        
        // Apply visual corruption
        const corruptionLevel = Math.floor(memory.corruptionLevel / 10);
        memoryCard.className = `memory-card corrupted-${corruptionLevel}`;
        
        // Corrupt text content
        if (memory.corruptionLevel > 20) {
            this.corruptText(memory);
        }
        
        // Disable save button if too corrupted
        if (memory.corruptionLevel > 80) {
            const saveBtn = memoryCard.querySelector('.save-btn');
            if (saveBtn && !saveBtn.disabled) {
                saveBtn.disabled = true;
                saveBtn.textContent = '💀 Too corrupted';
                saveBtn.style.background = '#333';
            }
        }
        
        // Add severe glitch effects
        if (memory.corruptionLevel > 60) {
            memoryCard.classList.add('critical-corruption');
        }
        
        if (memory.corruptionLevel > 90) {
            memoryCard.classList.add('death-throes');
        }
    }

    corruptText(memory) {
        const contentElement = document.getElementById(`content-${memory.id}`);
        if (!contentElement) return;
        
        let text = memory.content;
        const corruptionRate = memory.corruptionLevel / 100;
        
        // Replace characters with corruption symbols
        const corruptionChars = ['█', '▓', '▒', '░', '▄', '▀', '■', '□'];
        let corruptedText = '';
        
        for (let char of text) {
            if (Math.random() < corruptionRate * 0.3) {
                corruptedText += corruptionChars[Math.floor(Math.random() * corruptionChars.length)];
            } else {
                corruptedText += char;
            }
        }
        
        contentElement.innerHTML = corruptedText;
        
        // Add glitch classes
        if (Math.random() < corruptionRate) {
            contentElement.classList.add('glitch-text');
        }
    }

    addRandomGlitch(element) {
        const glitchClasses = ['glitch-text', 'glitch-rgb', 'glitch-static', 'vhs-distort'];
        const randomGlitch = glitchClasses[Math.floor(Math.random() * glitchClasses.length)];
        
        element.classList.add(randomGlitch);
        
        setTimeout(() => {
            element.classList.remove(randomGlitch);
        }, 200 + Math.random() * 800);
    }

    addRandomGlobalGlitch() {
        const body = document.body;
        const glitchClasses = ['glitch-scanlines', 'vhs-distort'];
        const randomGlitch = glitchClasses[Math.floor(Math.random() * glitchClasses.length)];
        
        body.classList.add(randomGlitch);
        
        setTimeout(() => {
            body.classList.remove(randomGlitch);
        }, 100 + Math.random() * 300);
    }

    updateCorruptionBasedOnScroll() {
        const scrollSpeed = Math.abs(window.scrollY - this.lastScrollY);
        
        if (scrollSpeed > 50) {
            // Fast scrolling accelerates corruption
            this.loadedMemories.forEach(memory => {
                if (!memory.saved) {
                    memory.corruptionLevel += scrollSpeed * 0.01;
                }
            });
        }
    }

    accelerateCorruption() {
        this.loadedMemories.forEach(memory => {
            if (!memory.saved) {
                memory.corruptionLevel += 1 + Math.random() * 2;
            }
        });
    }

    updateScrollResistance() {
        // Scrolling becomes harder as internet dies
        this.scrollResistance = 1 + (100 - this.internetIntegrity) * 0.05;
    }

    updateCountdown() {
        const minutes = Math.floor(this.timeRemaining / 60);
        const seconds = this.timeRemaining % 60;
        const timeString = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        document.getElementById('countdown').textContent = timeString;
        
        // Change color as time runs out
        const countdownElement = document.getElementById('countdown');
        if (this.timeRemaining < 60) {
            countdownElement.style.color = '#ff4444';
            countdownElement.style.animation = 'pulse 0.5s infinite';
            
            // Show apocalyptic warnings
            if (this.timeRemaining === 30) {
                this.showApocalypseWarning('THE END IS NEAR', 'Only 30 seconds left until digital death');
            } else if (this.timeRemaining === 10) {
                this.showApocalypseWarning('FINAL MOMENTS', 'Internet integrity failing...');
            }
        } else if (this.timeRemaining < 180) {
            countdownElement.style.color = '#ff8844';
            
            if (this.timeRemaining === 120) {
                this.showApocalypseWarning('CRITICAL STATE', 'Less than 2 minutes remaining');
            }
        }
        
        // Mid-game warnings
        if (this.timeRemaining === 300) {
            this.showApocalypseWarning('HALFWAY POINT', 'The internet is 50% dead');
        }
    }
    
    showApocalypseWarning(title, message) {
        const warning = document.createElement('div');
        warning.className = 'apocalypse-warning';
        warning.innerHTML = `
            <div class="warning-title">${title}</div>
            <div class="warning-message">${message}</div>
        `;
        
        document.body.appendChild(warning);
        
        // Add dramatic entrance
        setTimeout(() => warning.classList.add('show'), 100);
        
        // Remove after 3 seconds
        setTimeout(() => {
            warning.classList.remove('show');
            setTimeout(() => warning.remove(), 500);
        }, 3000);
    }

    getVisibleMemories() {
        const visibleMemories = [];
        const viewportTop = window.scrollY;
        const viewportBottom = viewportTop + window.innerHeight;
        
        this.loadedMemories.forEach(memory => {
            const element = document.getElementById(`memory-${memory.id}`);
            if (element) {
                const rect = element.getBoundingClientRect();
                const elementTop = rect.top + window.scrollY;
                const elementBottom = elementTop + rect.height;
                
                if (elementTop < viewportBottom && elementBottom > viewportTop) {
                    visibleMemories.push(memory);
                }
            }
        });
        
        return visibleMemories;
    }

    endWorld() {
        this.isEnded = true;
        clearInterval(this.corruptionTimer);
        clearInterval(this.fastCorruptionTimer);
        clearInterval(this.ghostActivityTimer);
        
        // Final corruption wave
        this.loadedMemories.forEach(memory => {
            if (!memory.saved) {
                memory.corruptionLevel = 100;
                const memoryCard = document.getElementById(`memory-${memory.id}`);
                if (memoryCard) {
                    memoryCard.classList.add('death-throes');
                }
            }
        });
        
        // Show end screen after dramatic pause
        setTimeout(() => {
            this.showEndScreen();
        }, 2000);
    }

    // Ghost Users - create feeling of shared apocalypse
    initializeGhostUsers() {
        const ghostNames = [
            'digital_refugee_2847',
            'memory_keeper_lost',
            'AnonymousArchiver',
            'last_librarian',
            'data_shepherd_99',
            'CyberNostalgia',
            'forgotten_username',
            'archive_angel',
            'bit_preserver',
            'echo_in_the_void'
        ];
        
        this.ghostUsers = ghostNames.map(name => ({
            username: name,
            savesRemaining: Math.floor(Math.random() * 20) + 5,
            lastAction: Date.now() - Math.random() * 60000
        }));
    }
    
    startGhostActivity() {
        this.ghostActivityTimer = setInterval(() => {
            if (this.isEnded) return;
            
            // Random ghost user activity
            if (Math.random() < 0.3) {
                this.simulateGhostAction();
            }
        }, 3000 + Math.random() * 7000);
    }
    
    simulateGhostAction() {
        const availableMemories = this.loadedMemories.filter(m => !m.saved && m.corruptionLevel < 80);
        if (availableMemories.length === 0) return;
        
        const randomMemory = availableMemories[Math.floor(Math.random() * availableMemories.length)];
        const randomGhost = this.ghostUsers[Math.floor(Math.random() * this.ghostUsers.length)];
        
        if (randomGhost.savesRemaining <= 0) return;
        
        const actions = [
            () => this.showGhostSave(randomMemory, randomGhost),
            () => this.showGhostFailedSave(randomMemory, randomGhost),
            () => this.showGhostViewing(randomMemory, randomGhost)
        ];
        
        const randomAction = actions[Math.floor(Math.random() * actions.length)];
        randomAction();
    }
    
    showGhostSave(memory, ghost) {
        const memoryCard = document.getElementById(`memory-${memory.id}`);
        if (!memoryCard) return;
        
        const ghostMessage = document.createElement('div');
        ghostMessage.className = 'ghost-message save';
        ghostMessage.innerHTML = `💾 ${ghost.username} saved this memory`;
        
        memoryCard.appendChild(ghostMessage);
        
        setTimeout(() => {
            ghostMessage.remove();
        }, 3000);
        
        ghost.savesRemaining--;
    }
    
    showGhostFailedSave(memory, ghost) {
        const memoryCard = document.getElementById(`memory-${memory.id}`);
        if (!memoryCard) return;
        
        const ghostMessage = document.createElement('div');
        ghostMessage.className = 'ghost-message failed';
        ghostMessage.innerHTML = `💀 ${ghost.username} tried to save this but ran out of saves`;
        
        memoryCard.appendChild(ghostMessage);
        
        setTimeout(() => {
            ghostMessage.remove();
        }, 4000);
    }
    
    showGhostViewing(memory, ghost) {
        const memoryCard = document.getElementById(`memory-${memory.id}`);
        if (!memoryCard) return;
        
        const ghostMessage = document.createElement('div');
        ghostMessage.className = 'ghost-message viewing';
        ghostMessage.innerHTML = `👁️ ${ghost.username} is viewing this memory`;
        
        memoryCard.appendChild(ghostMessage);
        
        setTimeout(() => {
            ghostMessage.remove();
        }, 2000);
    }

    showEndScreen() {
        const endScreen = document.getElementById('end-screen');
        const totalMemories = this.memories.length;
        const lostMemories = totalMemories - this.savedMemories.length;
        
        document.getElementById('saved-count').textContent = this.savedMemories.length;
        document.getElementById('lost-count').textContent = lostMemories.toLocaleString();
        
        endScreen.classList.remove('hidden');
        
        // Add final glitch effects
        endScreen.classList.add('emergency-glitch');
        setTimeout(() => {
            endScreen.classList.remove('emergency-glitch');
        }, 1000);
    }
}

// Vault functionality
function showVault() {
    const vaultModal = document.getElementById('vault-modal');
    const vaultItems = document.getElementById('vault-items');
    
    vaultItems.innerHTML = '';
    
    if (apocalypse.savedMemories.length === 0) {
        vaultItems.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #666;">
                <p>Your vault is empty.</p>
                <p>No memories have been preserved.</p>
            </div>
        `;
    } else {
        apocalypse.savedMemories.forEach(memory => {
            const vaultItem = document.createElement('div');
            vaultItem.className = 'vault-item';
            vaultItem.innerHTML = `
                <div class="memory-header">
                    <span class="memory-type">${memory.type}</span>
                    <span class="memory-year">${memory.year}</span>
                </div>
                <div class="memory-content">${memory.content}</div>
                <div class="memory-author">@${memory.author}</div>
            `;
            vaultItems.appendChild(vaultItem);
        });
    }
    
    vaultModal.classList.remove('hidden');
}

function closeVault() {
    document.getElementById('vault-modal').classList.add('hidden');
}

function restart() {
    location.reload();
}

// Initialize the apocalypse
let apocalypse;
document.addEventListener('DOMContentLoaded', () => {
    apocalypse = new DigitalApocalypse();
});

// Add some ambient effects on load
window.addEventListener('load', () => {
    // Subtle screen flicker on load
    document.body.style.animation = 'staticNoise 0.1s';
    setTimeout(() => {
        document.body.style.animation = '';
    }, 100);
});